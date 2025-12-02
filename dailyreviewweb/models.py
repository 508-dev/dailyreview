from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Prompt(models.Model):
    """
    A global question that all users can answer.
    Example: "When did you feel sad?"
    """
    text = models.CharField(max_length=1000)
    # Optional longer description or guidance text if you want it later
    help_text = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class EntryType(models.TextChoices):
    NORMAL = "normal", "Normal"
    SUMMARY_WEEK = "summary_week", "Weekly summary"
    SUMMARY_MONTH = "summary_month", "Monthly summary"
    SUMMARY_YEAR = "summary_year", "Yearly summary"


class Entry(models.Model):
    """
    A single journal entry: either a normal response to a prompt,
    or a summary over a period (week/month/year).
    """

    # Which user wrote this entry
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    # Which prompt this entry is answering
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name="entries",
    )

    # What kind of entry is this? Normal daily one, or a summary?
    entry_type = models.CharField(
        max_length=20,
        choices=EntryType.choices,
        default=EntryType.NORMAL,
    )

    # The actual journal text. Can be blank if you want client to handle "empty" entries.
    content = models.TextField(blank=True)

    # The date this entry is *about* (e.g. "today's answer").
    # For a weekly summary, this could be the day they wrote it, or period_start.
    entry_date = models.DateField()

    # When it was created/updated in the system.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # For summary entries, the period they summarize (optional for normal entries).
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-entry_date", "-created_at"]
        # unique "weekly summary" per user + prompt + period_start
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=["user", "prompt", "entry_type", "period_start"],
        #         name="unique_period_summary_per_prompt_user",
        #         condition=models.Q(entry_type__in=[
        #             EntryType.SUMMARY_WEEK,
        #             EntryType.SUMMARY_MONTH,
        #             EntryType.SUMMARY_YEAR,
        #         ]),
        #     )
        # ]

    def __str__(self):
        return f"{self.user} – {self.prompt} – {self.entry_date} ({self.entry_type})"

    @property
    def is_summary(self) -> bool:
        return self.entry_type != EntryType.NORMAL

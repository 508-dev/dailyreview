# Daily Review App

An app for answering daily review questions.

## Local Dev

`python -m venv .venv`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

Prompts have a foreign relationship to Container. One Container can have many Prompts.
Entries have a foreign relationship to Prompts (and vice versa?). One Prompt can have many Entries (but one per user). Entries are related to users: One user can have many Entries, one Entry can only be related to one User.

Something like

```
entry:
{
    text: 'I felt happy when I saw my dog'
    created_on: (some timestamp)
    updated_on: (some timestamp)
}

prompt: {
        text: 'When did you feel happy?"
}

container: {
           scope: (one of day, week, month)
           date: (either a specific day, or, a week number + year, or, a month + year)
}



GET prompts/

[{text: 'When did you feel happy?'} {text: 'When did you feel sad?'}]

GET user/{id}/entries

[{text: 'I felt happy when i saw my dog', created_on: {}, updated_on: {}, prompt: {id}]

GET user/{id}/entries?prompt={id}

[{text: 'I felt happy when i saw my dog', created_on: {}, updated_on: {}, prompt: {id}}, {text: 'I felt happy when I ate an apple',created_on: {}, updated_on: {}, prompt: {id}}]

GET user/{id}/entries?date={date}
Return Entries for that date.

GET user/{id}/entries?prompt_

POST entries/

[{text: 'I felt happy when i saw my dog', prompt: {id1}}, {text: 'I felt sad when I broke my mug.', prompt: {id}}]

```

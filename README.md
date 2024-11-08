# Repro for issue 7365

## Versions

firebase-tools: v13.24.1<br>
node: v20.12.2<br>
platform: macOS Sonoma 14.7

## Setup

1. Run `cd functions`
1. Run `python3.12 -m venv venv`
1. Run `. "/Users/<path>functions/venv/bin/activate" && python3.12 -m pip install -r requirements.txt`

## Steps to reproduce

1. Run `firebase deploy --only functions --project PROJECT_ID`
   - Error is raised, however, the `dummy_function` is deployed

```
i  functions: creating Python 3.12 (2nd Gen) function dummy_function(us-central1)...
HTTP Error: 400, Queue ID "dummy_function" can contain only letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). Queue ID must be between 1 and 100 characters.

Functions deploy had errors with the following functions:
        dummy_function(us-central1)
i  functions: cleaning up build files...

Error: There was an error deploying functions
```

2. Rename `dummy_function` to `dummy` in functions/main.py
3. Run `firebase deploy --only functions --project PROJECT_ID`
   - ? Would you like to proceed with deletion? Selecting no will continue the rest of the deployments. (Yes)

```
? Would you like to proceed with deletion? Selecting no will continue the rest of the deployments. Yes
i  functions: creating Python 3.12 (2nd Gen) function dummy(us-central1)...
i  functions: deleting Python 3.12 (2nd Gen) function dummy_function(us-central1)...
HTTP Error: 400, Queue ID "dummy_function" can contain only letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). Queue ID must be between 1 and 100 characters.
✔  functions[dummy(us-central1)] Successful create operation.

Functions deploy had errors with the following functions:
        dummy_function(us-central1)j
i  functions: cleaning up build files...

Error: There was an error deploying functions
```

## Notes

When trying to delete the function using `firebase functions:delete dummy_function --project PROJECT_ID`, same error is raised

```
$ functions:delete dummy_function
? You are about to delete the following Cloud Functions:
        dummy_function(us-central1)
  Are you sure? Yes
i  functions: deleting Python 3.12 (2nd Gen) function dummy_function(us-central1)...
HTTP Error: 400, Queue ID "dummy_function" can contain only letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). Queue ID must be between 1 and 100 characters.

Functions deploy had errors with the following functions:
        dummy_function(us-central1)
i  functions: cleaning up build files...
```

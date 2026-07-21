# Workflows

## General workflow

User --> Upload CV or Resume --> Extract Text --> Save --> Upload JD --> Scoring --> Result --> Interview question

## Signup & Signin flow

User --> Username & Password --> Hash password --> Verify --> Access or reject.

## Upload CV or resume flow

User --> choose mode upload (file, manual) --> Validate --> Extract --> Save CV or not --> Return ID

**Detail:**

**- Resume upload**

POST /resume/upload
Parameter:
- file
- cv_name

│

Validate file

│

Generate UUID

│

Upload file (Local → sau này AWS S3)

│

Create Resume
(status = PENDING)

│

Fake Parser

│

Update Resume
(parsed_text, status = READY)

│

Return Response

## Upload JD flow

User --> User --> choose mode upload (file, manual)  --> Validate --> Extract --> Save JD or not --> Return ID

POST /job-descrip/upload
Parameter:
- file
- jd_name

│

Validate file

│

Generate UUID

│

Upload file (Local → sau này AWS S3)

│

Create Resume
(status = PENDING)

│

Fake Parser

│

Update Resume
(parsed_text, status = READY)

│

Return Response

## Scoring flow (research)

\-------

## Result (research)

\-------

## Interview question (research)

\------
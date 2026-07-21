# Project structure

## **Summary**

This file descrise folder tree of this project. Each file or folder are descrise follow request life cycle.

HTTP Request  
     │  
     ▼  
Router (api)  
     │  
     ▼  
Service  
     │  
     ▼  
Repository  
     │  
     ▼  
Database

---

## **Folder tree**

---

\-.  
├── app  
│   ├── api  
│   ├── core  
│   ├── db  
│   ├── features  
│   │   ├── auth  
│   │   ├── job-descri  
│   │   └── resume  
│   └── main.py  
├── docs  
│   ├── data-structure.md  
│   ├── decisions  
│   ├── flow.md  
│   ├── images  
│   ├── product.md  
│   └── project-structure.md  
├── personal-docs.md  
├── scripts  
└── tests

---

## **Description**

Role of each file in project.

app

*   Main folder of project, contain all project file.
*   router: endpoint of this feature, colab with api folder
*   service: busines logic, recieve input, excute logic, call responsitory.
*   Model: DB model, use for SQLmodel, ORM, migration, etc. 
*   Schema: model for api. Validate input, define response.

Router


↓

Request Schema (Pydantic)


↓

Service


↓

Resume (SQLModel) -> lâấ model từ SQLModel vì nó tieế xuú voớ repo


↓

Repository

api

*   Contain API endpoint of project.
*   Recieve request, validate input.
*   Call service, return response

core

*   Contain business used in through all project. Such as JWT, middleware, Setting, etc.

db

*   Contain DB.
*   Engine, BaseModel, migration

docs

*   Document of project

scripts

*   Containt Iaas code or setup linux script
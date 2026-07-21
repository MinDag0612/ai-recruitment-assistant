#   File containt tool used in this project  !!
This project i use uv
##   Working flow using UV
- uv add
- uv remove
- uv sync
- uv run

##  Using ORM
Viết Python Model

↓

Alembic sinh Migration

↓

Migration tạo Table

##  using Alembic to manage migrate DB
- alembic.ini: Config of Alembic
- migrations/versions: history migration
- env.py: DB model
- script.py.mako: template -> ko suủa

Run script: **uv run alembic init migrations**

**target_metadata = SQLModel.metadata**
This is variable to Alembic know where model db stored. When SQLModel run , metadata is used for stored model data. Alembic read that to know how DB design.

① Model (Python)

↓

② Migration (Lịch sử thay đổi)

↓

③ Database (Thực tế)

**alembic revision --autogenerate -m "initial schema"**

--> This script create provision table base on designed mode

Note:
- import sqlmodel is not exist
- Helpfull when work in group
  - Table alembic version is created to Alembic know what version created and update to head easily

**alembic upgrade head**  


##   Setup file config to manage project varriable
- BaseSetting is used for get value from Env
- SettingsConfigDict is used for config BaseSetting
- using:
  - **from app.core.config import settings**
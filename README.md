## fatapi-nlp

#### Run  
  
```bash
# set execution plicies
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# activate env 
./venv-api/Scripts/Activate.ps1

# copy .env file
cp .env_example .env

# run api
fastapi dev ./app/main.py


```

#### Use the api

```bash

curl http://localhost:8000/api/v1/autocomplete?query=My%20name%20is

```
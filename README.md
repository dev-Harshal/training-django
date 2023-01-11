## Atomicloops Django Setup

### Project-Name : training

### 1. Clone the repository

```
git clone https://github.com/atomic-loops/training-django
cd training-django
git checkout -b dev
```

### 2. Install AWS CLI and configurations as per your os

- [Install AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Install & Configure AWSCLI](https://medium.com/analytics-vidhya/configure-aws-cli-and-execute-commands-fc16a17b0aa2)

### 3. Create a new virtualenv and install requirements

- [How to install virtualenv](https://drive.google.com/file/d/1D8UGYytOoTfe4WjsIZQtZm4psu1YolNC/view?usp=share_link)

#### Windows

```
virtualenv venv
.\venv\Scripts\activate
pip install atomicloops_django-1.0-py3-none-any.whl 
pip install -r requirements.txt
pip install "drf-yasg[validation]"
pip install git+https://github.com/atomic-loops/atomicloops-django-logger
```

#### Linux and Mac OS

```
virtualenv venv
source venv/bin/activate
pip install atomicloops_django-1.0-py3-none-any.whl 
pip install -r requirements.txt
pip install "drf-yasg[validation]"
pip install git+https://github.com/atomic-loops/atomicloops-django-logger
```

### 4. Download vault file

A. Initial

```
wget -O src/vault.py https://video-data-wget.s3.us-east-2.amazonaws.com/vault.py
```

Windows

```
curl -o src/vault.py https://video-data-wget.s3.us-east-2.amazonaws.com/vault.py
```

B. Latest

```
wget -O src/vault.py https://video-data-wget.s3.us-east-2.amazonaws.com/vault.py
```

Windows

```
curl -o src/vault.py https://video-data-wget.s3.us-east-2.amazonaws.com/vault.py
```

Note :- Update the urls for Lastest Section when you sync the vault file.

### 5. Initialize Project Setup

[Atomicloops Django Setup](https://drive.google.com/file/d/1lQ4udUgGdZOCro4z41W1K2qy5HzgNJWd/view?usp=share_link)

### 6. Makemigrations and Create Table

```
python manage.py run --mode interactive-dev
python manage.py makemigrations
python manage.py migrate
```

### 7. Atomicloops Custom Commands

[Atomicloops Custom Commands Document](https://drive.google.com/file/d/1dKK_Eo-7OAAFYTrEtS_N5pQGDLK06Y-a/view?usp=share_link)

### 8. Update and Sync Vault

To Add Secret key add the variable to vault file.

```
python manage.py sync-vault
```

### 9. How to add new libraries

```
source venv/bin/activate
pip install <package_name>
pip freeze > requirements.txt
```


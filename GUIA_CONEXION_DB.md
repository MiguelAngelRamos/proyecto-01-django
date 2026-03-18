## 1. Instalar la dependencia (Tener activado el entorno virtual)

```shell
pip install psycopg2-binary
```

## 2. Crear la base de datos en PostgreSQL

```sql
CREATE DATABASE minimarket_sofia;
```

> **IMPORTANTE** Django no crea la base de datos, solo crea las tablas de una base de datos que ya exista.

## 3. Ir al archivo de configuración en nuestro caso (core/settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'minimarket_sofia',
        'USER': 'postgres',
        'PASSWORD': 'academy',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 4. Motor de sessiones (SESSION_ENGINE)

```python
# Sesiones se almacenan en una tabla llamada django_session de PostgreSQL
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
```


## 5. Generar y aplicar Migraciones

```shell
python manage.py makemigrations catalogo
```
```shell
python manage.py makemigrations bodega
```
```shell
python manage.py migrate
```

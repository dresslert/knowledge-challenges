from __future__ import print_function
import logging
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context
from database import Base  # Importa a Base do arquivo database.py
from models import *  # Importa todos os modelos

# Configurações do Alembic
config = context.config

# Adiciona o URL do banco de dados
config.set_main_option('sqlalchemy.url', 'sqlite:///./test.db')

target_metadata = Base.metadata

def run_migrations_offline():
    """ Executa migrações no modo offline. """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """ Executa migrações no modo online. """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

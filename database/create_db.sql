CREATE TABLE client
(
    clientname VARCHAR(64) PRIMARY KEY,
    mail VARCHAR(64) NOT NULL,
    password VARCHAR(128) NOT NULL,
    name VARCHAR(64) NOT NULL,
    surname VARCHAR(64) NOT NULL,
    birth DATE NOT NULL,
    image VARCHAR(64) NOT NULL DEFAULT 'default',
    position VARCHAR(64) NOT NULL DEFAULT 'customer',
    work_time INTEGER DEFAULT 0
);

CREATE TABLE task
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(64) NOT NULL,
    description TEXT,
    completion_date TIMESTAMP,
    state SMALLINT NOT NULL DEFAULT 0,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    worker_id VARCHAR(64) REFERENCES client(clientname),
    creator_id VARCHAR(64) REFERENCES client(clientname),
    based_on VARCHAR(64) REFERENCES ticket(id)
);

CREATE TABLE product
(
    name VARCHAR(64) PRIMARY KEY,
    description TEXT,
    image VARCHAR(64) DEFAULT 'default',
    creation_date DATE DEFAULT CURRENT_DATE,
    completion_date DATE,
    version VARCHAR(64),
    manager_id VARCHAR(64) REFERENCES client(clientname)
);

CREATE TABLE ticket
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    description TEXT NOT NULL,
    state SMALLINT NOT NULL DEFAULT 0,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image VARCHAR(64),
    author_id VARCHAR(64) REFERENCES client(clientname),
    product_name VARCHAR(64) REFERENCES product(name)
);

CREATE TABLE comment
(
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    image VARCHAR(64),
    ticket_id SERIAL REFERENCES ticket(id),
    author_id VARCHAR(64) REFERENCES client(clientname)
);

CREATE TABLE product_customer
(
    state SMALLINT NOT NULL DEFAULT 0,
    customer_id VARCHAR(64) REFERENCES client(clientname),
    product_id VARCHAR(64) REFERENCES product(name)
);

CREATE USER iis_webapp WITH ENCRYPTED PASSWORD 'iis_passwd';
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO iis_webapp;

COMMIT;

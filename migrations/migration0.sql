DROP TABLE IF EXISTS Owner;
CREATE TABLE Owner (
    name varchar(255),
    followers int,
    PRIMARY KEY (name)
);

DROP TABLE IF EXISTS User;
CREATE TABLE User (
	name varchar(255),
    following int,
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES Owner(name)
);

DROP TABLE IF EXISTS Organization;
CREATE TABLE Organization (
	name varchar(255),
    PRIMARY KEY (name),
    FOREIGN KEY (name) REFERENCES Owner(name)
);


DROP TABLE IF EXISTS OrganizationUser;
CREATE TABLE OrganizationUser (
    user_name varchar(255),
    organization_name varchar(255),
    PRIMARY KEY (user_name, organization_name),
    FOREIGN KEY (user_name) REFERENCES User(name),
    FOREIGN KEY (organization_name) REFERENCES Organization(name)
);

DROP TABLE IF EXISTS Repository;
CREATE TABLE Repository (
	name varchar(255),
    stars int,
    forks int,
    watching int,
    owner varchar(255),
    PRIMARY KEY (name, owner),
    FOREIGN KEY (owner) REFERENCES Owner(name)
);

DROP TABLE IF EXISTS File;
CREATE TABLE File (
    id int AUTO_INCREMENT,
    name varchar(255),
    language varchar(255),
    path varchar(255),
    repo_name varchar(255),
    owner varchar(255),
    PRIMARY KEY (id, repo_name, owner),
    FOREIGN KEY (repo_name, owner) REFERENCES Repository(name, owner)
);

DROP TABLE IF EXISTS Issue;
CREATE TABLE Issue (
	id int AUTO_INCREMENT,
    check_id varchar(255),
    start_line int,
    end_line int,
    category varchar(255),
    impact varchar(255),
    repo_name varchar(255),
    owner varchar(255),
    file_id int,
    PRIMARY KEY (id, repo_name, owner, file_id),
    FOREIGN KEY (file_id, repo_name, owner) REFERENCES File(id, repo_name, owner)
);

DROP TABLE IF EXISTS Contributor;
CREATE TABLE Contributor (
    user_name varchar(255),
    repo_name varchar(255),
    owner varchar(255),
    PRIMARY KEY (user_name, repo_name, owner),
    FOREIGN KEY (user_name) REFERENCES User(name),
    FOREIGN KEY (repo_name, owner) REFERENCES Repository(name, owner)
);

DROP TABLE IF EXISTS RepositoryQueue;
CREATE TABLE RepositoryQueue (
    repo_name varchar(255),
    owner varchar(255),
    date_inserted datetime,
    PRIMARY KEY (repo_name, owner),
    FOREIGN KEY (repo_name, owner) REFERENCES Repository(name, owner)
);

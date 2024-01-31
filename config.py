from configparser import ConfigParser


# Pre-pare Dabase Information from configuration file.
def config(filename="database.ini", section="postgresql"):
    parser = ConfigParser()

    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        # params
        # [('host', 'localhost'), ('database', 'db1'), ('user', 'postgres'), ('password', 'admin'), ('port_id', '5432')]
        for param in params:
            db[param[0]] = param[1]
    
    else:
        raise Exception(f"Section {section} is not found in the {filename} file.")
    
    return db
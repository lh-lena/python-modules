

def list_to_dict() -> dict:
    # Given list of tuples
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    # Convert list of tuples into a dictionary
    musicians_dict = {}
    for name, year in d:
        # If the year already exists as a key, append the name to the list of names
        if year in musicians_dict:
            musicians_dict[year] += f" {name}"
        else:
            musicians_dict[year] = name
    return musicians_dict
    

def main():
    musicians_dict = list_to_dict()
    # Display the dictionary in the required format
    for year in sorted(musicians_dict):
        print(f"{year} : {musicians_dict[year]}")

if __name__ == "__main__":
    main()

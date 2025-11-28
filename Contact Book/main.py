import json


CONTACT_BOOK = r'Python-Training/Contact Book/book.json'

def load_contacts():
    try:
        with open(CONTACT_BOOK,'r') as  file :
            contacts = json.load(file)
    except FileNotFoundError:
        print("file not found")
    return contacts


def view_contacts(contacts):
    if not  contacts:
        print("no contact available")
    else:
        for names,info in contacts.items():
            print(" ")
            print(f"Name: {names}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(" ")


def save_contacts(contacts):
        with open(CONTACT_BOOK,'w') as  file :
            json.dump(contacts,file,indent=4)



def add_contacts(contacts):
    name = input("enter ur name : ")
    phone= input("enter your phone :")
    email= input ("enter your email : ")
    
    contacts[name] = {"phone":phone,"email":email }
    save_contacts(contacts)
    print(" Contact Added ")

def remove_contact(contacts):
    name= input("enter name to del : ")
    del contacts[name]
    save_contacts(contacts)
    print(" Contact Removed ")

    


def main():
    while True:
        contacts = load_contacts()

        print("\n")
        print("contact book menu ")
        print(" 1 to view contact")
        print(" 2 to add contact")
        print(" 3 to remove contact")
        print(" 4 to exit")
        print("\n")

        choice = int(input("enter the no 1-4 : "))

        if choice == 1 :
            print(view_contacts(contacts))
        elif choice == 2 :
            add_contacts(contacts)
        elif choice ==3 :
            remove_contact(contacts)
        elif choice == 4 :
            print("Good byee ")
            break




if __name__ == "__main__":      
        main()
    
  


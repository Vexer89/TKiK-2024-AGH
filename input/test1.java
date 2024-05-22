import java.util.ArrayList;
import java.util.Scanner;

class Contact {
    private String name;
    private String phoneNumber;
    private String email;

    public Contact(String name, String phoneNumber, String email) {
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "Name: " + name + ", Phone Number: " + phoneNumber + ", 
Email: " + email;
    }
}

public class ContactManager {
    private ArrayList<Contact> contacts;
    private Scanner scanner;

    public ContactManager() {
        contacts = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public void addContact() {
        System.out.println("Enter contact name:");
        String name = scanner.nextLine();
        System.out.println("Enter contact phone number:");
        String phoneNumber = scanner.nextLine();
        System.out.println("Enter contact email:");
        String email = scanner.nextLine();
        Contact contact = new Contact(name, phoneNumber, email);
        contacts.add(contact);
        System.out.println("Contact added successfully!");
    }

    public void removeContact() {
        System.out.println("Enter the name of the contact to remove:");
        String name = scanner.nextLine();
        Contact contactToRemove = null;
        for (Contact contact : contacts) {
            if (contact.getName().equalsIgnoreCase(name)) {
                contactToRemove = contact;
                break;
            }
        }
        if (contactToRemove != null) {
            contacts.remove(contactToRemove);
            System.out.println("Contact removed successfully!");
        } else {
            System.out.println("Contact not found.");
        }
    }

    public void listContacts() {
        if (contacts.isEmpty()) {
            System.out.println("No contacts to display.");
        } else {
            System.out.println("Contact List:");
            for (Contact contact : contacts) {
                System.out.println(contact);
            }
        }
    }

    public void showMenu() {
        while (true) {
            System.out.println("\nContact Manager");
            System.out.println("1. Add Contact");
            System.out.println("2. Remove Contact");
            System.out.println("3. List Contacts");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");

            int choice = Integer.parseInt(scanner.nextLine());
            switch (choice) {
                case 1:
                    addContact();
                    break;
                case 2:
                    removeContact();
                    break;
                case 3:
                    listContacts();
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid choice. Please try 
again.");
            }
        }
    }

    public static void main(String[] args) {
        ContactManager contactManager = new ContactManager();
        contactManager.showMenu();
    }
}


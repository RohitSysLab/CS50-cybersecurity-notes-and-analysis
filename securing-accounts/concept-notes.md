
# Securing Accounts – CS50 Cybersecurity

## 1. Core Idea

Authentication is the process of knowing whether someone is truly who they claim to be before granting access.

sometimes security is overlooked in a software or program not because of lack of technical expertise but because of user behaviour and usability

## 2. Key Concepts

### Authentication vs Authorization
- Authentication: Are you who you say you are?
- Authorization: What are you allowed to access?

### Password Storage
- Passwords are often stored in structured datasets.
- Attackers can use dictionary attacks by trying common words.

### Dictionary Attack
An attacker uses a predefined list of likely passwords to attempt access.

### Brute Force Attack
An attacker systematically tries all possible combinations using code.
Example: nested loops iterating through digits and ASCII letters constants

## 3. Technical Observation

A practical demonstration is implemented in `code/crack.py`.

The script simulates a brute force / dictionary-style password attempt by iterating through possible combinations programmatically.

This demonstrates:

- Weak passwords is easier to brute force 
- short passwords are mathematically vulnerable

## 4. Human Factor Problem

If passwords become too complex:
- Users may reuse passwords.
- Users may write them down.
- Users may abandon the system.

Security must balance strength and usability.

## 5. Deeper Reflection

The biggest vulnerability may not be the system — but human behavior.

Improving security often requires improving user habits, not just writing better code.

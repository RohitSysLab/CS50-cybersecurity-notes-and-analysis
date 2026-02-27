
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

### NIST(National Institute of standards and technology)
it is an organisation in USA that recommends guidelines and policy related to cybersecurity practices fo governments, companies and critical infrasstructure

### 2-Factor authentication
its a way of verification and authentication of identity using only two factors such as a password and something which we have such as codes generated in authenticator apps on our device 

### Multifactor-Authentication
it is a secure way of verification and authentication of identity using more than two factors, such as passwords,SMS,OTP,codes on authenticator app,biometric like fingerprint

## keylogger
keylogger is a programm that tracks keystroke or in other words it can track what we type on our device

usage:-attackers can use this kind of software/programm to send our typing habits or what we type on keyboards to remote servers via internet

## sim swapping attack
sim swapping is nothing more than convincing the mobile carrier to transfer the victim's phone number to another sim and gaining access to their bank account,social media, email. an attacker succeeds generally because of gathering opensource information about the victim 

## 3. Technical Observation

A practical demonstration is implemented in `code/crack.py`.

The script simulates a brute force / dictionary-style password attempt by iterating through possible combinations programmatically.

This demonstrates:

- Weak passwords is easier to brute force 
- short passwords are mathematically vulnerable

## 4. Human as a attack vector

If passwords become too complex:
- Users may reuse passwords.
- Users may write them down.
- Users may abandon the system.

Security must balance strength and usability.

## 5. Deeper Reflection

The biggest vulnerability may not be the system/Technology — but human behavior.

Improving security often requires improving user habits, not just writing better code.

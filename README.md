# Authomator
Automate login using sensitive info (login credentials) without compromising security and without using env variables.

![Screen Shot 2021-11-17 at 9 59 44 PM](https://user-images.githubusercontent.com/43297314/142343826-bf056b53-b17e-434e-8712-efe637fe3f92.png)



> ## Why was this made ❓
>
> GeforceNOW, I hate having to enter my cryptic password manually every single time
> It's easier for me to remember 10 digit code than 32 digit 🙂

> ## Is this safe? 🤔
> 
> The attacker needs first get access to the computer 💻
> 
> Then need to know code for each of the passwords saved on the data.json file; *yes each password can have seperate key* 🔐


> ## Security
> The key isn't saved (even as hash) there's no hash to crack!
> Brute force is still possible (will take a long time depending on key's length) 
>
> Recommended to use one random memorable sentence with 2 special numbers, 1 weird symbol as password.

---


Done:
  - Encryption, Decryption, Saving, Retriving and Tests for encrypt decrypt

Need to do:
  - Pyautogui integration
  - Create Pip package, binary or port to swift (mac app)



License: [MIT](https://github.com/Aayush9029/Authomator/blob/main/LICENSE)

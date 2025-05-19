# XSS Vulnerable Web Application

Bu proje, Stored XSS (Cross-Site Scripting) güvenlik açığını test ortamında exploit etmek amacıyla oluşturulmuş basit bir web uygulamasıdır.

Amaç

Bu uygulama, geliştiricilere ve güvenlik uzmanlarına XSS açıklarını test etme ve anlama imkanı sağlar. Eğitim ve araştırma amaçlıdır.


## Gereksinimler

- [Podman](https://podman.io/getting-started/installation)

## Stored XSS Zafiyetli Web Uygulaması Kurulum ve Çalıştırma

1. **Container imajını oluşturun:**

   ```bash
   podman build -t xss-app .

2. **Container'ı başlatın:**

   ```bash
   podman run -d -p 9090:80 --name xss-vuln xss-app

![resim](https://github.com/user-attachments/assets/716eae15-d81a-4ff5-94ea-26c36ad5833a)



3. **Tarayıcıdan uygulamaya erişin:**

   ```bash

   http://localhost:9090

![resim](https://github.com/user-attachments/assets/24d9a48c-3a95-4f61-96b4-f18024761c23)











## "Trigger of Admin Account" Kurulum ve Çalıştırma


1. **HTTP Sunucu Başlatın:**

   ```bash
   python3 -m http.server 5555


![resim](https://github.com/user-attachments/assets/ffa87b00-35f6-4a16-a801-1f72046e8da8)


![resim](https://github.com/user-attachments/assets/479f7f9e-d1a2-42c0-a9d8-0b1e161f15c6)






https://github.com/user-attachments/assets/b9ceb8fc-acad-4157-b82c-0c5c7f6596e0










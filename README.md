#  Tokugawa - Gourmet Restaurant Website (WIP)

**Tokugawa** is a web application currently in development for a high-end Japanese restaurant. The project is based on a modern architecture combining **Django (Python)** for the backend and **React, TypeScript, Tailwind CSS**, and **Material UI (MUI)** for the frontend. It aims to deliver a smooth, responsive, and elegant user experience, with dynamic and advanced features.

---

##  Current Status: In Progress

The site was initially built entirely using **classic Django** with **HTML/CSS templates** and **Tailwind CSS** to quickly validate the structure, views, database models, and core backend features.

This initial version allowed for:

-  Implementing Django models and business logic  
-  Testing forms, gallery, comment section, and routing  
-  Prototyping a consistent responsive design using Tailwind CSS  

---

## Why Move to React + TypeScript?

The migration to **React + TypeScript** at this stage is motivated by:

- **Backend stability**: Django logic is fully operational, allowing a clean decoupled frontend through a REST API  
- **Modular architecture**: React offers better separation of components and flexible state management (forms, filters, comments)  
- **Enhanced UX**: Features like image carousels, real-time comment updates, and menu filtering are better handled with React  
- **Continued use of Tailwind CSS**: Fast and consistent styling across the application  
- **Scalability**: A React + TypeScript base opens the door for a SPA or PWA version  

---

## ✅ Features Already Implemented (Django)

- Pages: Home, Reservations, Menu, Story, Contact  
- Models: Dishes, Categories, Reservations, Chefs, Comments  
- Static image gallery  
- Functional forms for reservations and contact  
- Responsive layout using **Tailwind CSS**  
- Classic Django views with integrated routing  

---

## 🔄 In Progress

-  Full frontend redesign using **React + TypeScript + Tailwind CSS + MUI**  
-  Dynamic gallery with zoom and navigation  
-  Real-time comment section  
-  Dynamically filterable/sortable menu  
-  JavaScript + backend validation for forms  
-  Secure REST endpoints using **Django REST Framework**  
-  Full Dockerization of the project  

---

## Planned Features

### Frontend

- **Online reservations**: Interactive form with date/time and dietary preference selection  
- **Interactive gallery**: Dynamic carousel with zoom (React)  
- **Comments section**: Real-time post/view/sort/moderate  
- **Dynamic menu**: Filter by category, sort by price/popularity  
- **Contact form**: Fully validated and responsive  
- **Responsive design**: Seamless navigation across all screen sizes  
- **Unified UI**: Styled using **Tailwind CSS** and **Material UI components**  

### Backend

- **Secure REST API**: Endpoints for managing reservations, comments, dishes, categories, and chef profiles  
- **Authentication and roles**: Admin/moderator access with protected routes  
- **Server-side validation**: Backend logic to enforce business rules  
- **Clear business logic**: Handles time slots, availability, capacity limits, etc.  
- **PostgreSQL integration** using Django ORM  
- **Full Docker support** for simplified deployment  

---

## Translation API Integration (Planned)

This project will include a **translation API** to dynamically support **multiple languages** for menus, forms, and user comments.

### Target Languages

- French  
- English  
- Japanese  

### Translation APIs Considered

- **DeepL** – high translation accuracy  
- **LibreTranslate** – open-source, free  
- **Google Translate API** – fast and versatile  

### Planned Usage

- Translation of REST API data on the Django backend  
- Client-side rendering based on selected user language  

---

## Technologies Used

- **Backend**: Django, Django REST Framework, PostgreSQL  
- **Frontend**: React, TypeScript, Tailwind CSS, Material UI (MUI)  
- **Tools**: Docker, Git, GitHub  
- **Assets**: Royalty-free images and videos for immersive ambiance  

---

> This project is developed iteratively, with a clear separation between backend and frontend, ensuring long-term maintainability and scalability.

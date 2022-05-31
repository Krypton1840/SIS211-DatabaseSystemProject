# Waddy - Project Documentation

### Team members:

`Mostafa Ibrahim Abdellatif `-`Youssef Mohamed Emam`-`Youssef Magdi Salah Eldin` 
### How to run:

In the source code directory run: `python gui.py`

#### Modules used:

- `tkinter`, `pyodbc` ,`fpdf` ,`python-decouple`
### Features:

##### For Both Admins and Clients:
-  Log in, Sign up (with validations) and Log out.
- Refresh the main page to get updates.
##### Admin's main page and functionalities:
- Generate trips with a trip for each hour for both `O25` and `52O` routes (if the route is operative) starting from `06:00 AM` till `22:00 PM` for the next day.
- Select and cancel/delete a trip of status of status`Not Completed`. If some clients had already booked that trip then their trip bookings will be cancelled, and a PDF report with the clients' names and phone numbers will be generated for the Admin to inform them of the trip cancellation.
- Select and change the route status (`Operative`/`InOperative`).
  - If a route was of status `Operative` and trips were generated.Then the Admin changed it to`InOperative` and there were upcoming trips of status `Not Completed` then a PDF Report would be generated for the Admin with trips ids. If some clients had already booked these trips, their trip bookings will be cancelled, and a PDF report with the clients' names and phone numbers will be generated for the Admin, with the trip id as the header for each list of clients in the report.
- Select and mark a trip as completed.
- Mark all trips as completed.
- View all clients that signed up.
- Add drivers and commuter buses (with validations).
- Select and update drivers and commuter buses.
- Delete a driver and a Commuter bus
  - If a driver had a trip of status `Not Completed`, it will be cancelled/deleted. If some clients had already booked that trip, then their trip bookings will be cancelled, and a PDF report with the clients' names and phone numbers will be generated for the Admin to inform them of the trip cancellation.
- Generate a meaningful PDF report of numbers and data beneficial for the admins and managers.

#####   





##### Client's main page and functionalities:

- View all upcoming available trips.
- Select and book a trip.
  - The client can book more than one seat on a trip by entering the number of seats.
  - If the client didn't enter how many seats he wanted to book, it defaults to 1.
- View all of his previous and recent trip bookings with trip fees calculated.
- Select and delete a trip booking only if the trip is of status `Not Completed`.
- Select and give a feedback on a completed trip he had booked.
  - Give the trip a rating.
  - Give the driver a rating.

##### Client's and Admin's Profiles:

- View profile.
- Edit profile details including the password.

----

---

### Screenshots:

#### Menu:



![image](https://user-images.githubusercontent.com/78238174/171256693-ef2d3143-dfe4-4d51-a1b1-f294afbfbf3a.png)

---





#### Sign up:



![image](https://user-images.githubusercontent.com/78238174/171257095-ebc786b4-638d-4d26-a963-570ffa5893c7.png)

![image](https://user-images.githubusercontent.com/78238174/171257164-9bf5c996-3c79-4a69-9488-6de9c0f187b1.png)

---





#### Main pages:



Admin's main page:

![image](https://user-images.githubusercontent.com/78238174/171266172-2a70c54a-4d06-4eeb-ba1b-544257e7c402.png)



Client's main page:

![image](https://user-images.githubusercontent.com/78238174/171257390-9a5d62cb-6665-40ea-bc8b-89ce53bd93b1.png)

---





#### Profiles:



View profile:

![image](https://user-images.githubusercontent.com/78238174/171257440-bb8e8804-238b-4157-a085-1729eec8586f.png)

![image](https://user-images.githubusercontent.com/78238174/171257469-f31769d1-df82-4ed4-a00e-6e353c30f9c3.png)







Edit profile:

![image](https://user-images.githubusercontent.com/78238174/171257495-ecdc3f9a-c31f-4ba5-bc01-2f042a638028.png)

![image](https://user-images.githubusercontent.com/78238174/171257515-638f1fa1-5491-434b-806f-13526451f566.png)

# Waddy - Project Documentation

### Team members:

`Mostafa Ibrahim Abdellatif `  `Youssef Mohamed Emam`  `Youssef Magdi Salah Eldin` 

`Omar Ahmed Badr`  `Ahmed Mohamed Mokhtar`

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



![image-20220531172728007](C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531172728007.png)

---





#### Sign up:



![image-20220531173426842](C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531173426842.png)

![image-20220531183413464](C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531183413464.png)

---





#### Main pages:



Admin's main page:

![image-20220531182619031](C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531182619031.png)



Client's main page:

![image-20220531182411482](C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531182411482.png)

---





#### Profiles:



View profile:

<img src="C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531182851686.png" alt="image-20220531182851686" style="zoom:60%;" />

<img src="C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531183108560.png" alt="image-20220531183108560" style="zoom:60%;" />







Edit profile:

<img src="C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531182929260.png" alt="image-20220531182929260" style="zoom:60%;" />

<img src="C:\Users\corvus\AppData\Roaming\Typora\typora-user-images\image-20220531183150937.png" alt="image-20220531183150937" style="zoom:60%;" />
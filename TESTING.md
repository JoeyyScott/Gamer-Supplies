## Testing

### Bugs
+ **Review Carousel**:
    + Upon adding this feature it worked when there was one review in the list. When adding another review, the two reviews were displaying simultaneously as Bootstrap uses the ```active``` class to determine what to show.
    + After researching around I found [this post](https://stackoverflow.com/questions/35836879/how-to-use-for-loop-with-bootstrap-carousel) which utilized a for loop inside the inner carousel to only render active for the first iteration in the loop.
        + The code stated was ```{% if forloop.counter == 1 %}active{% endif %}``` which I adapted to check for the first review.

+ **Carousel auto scrolling**:
    + When adding in the carousel it was auto scrolling which I wanted to remove according to the assessment handbook about aggressive autoplaying of content.
        + I consulted the Bootstrap docs and when reading about interval I noticed in the below article [here](https://getbootstrap.com/docs/5.0/components/carousel/#disable-touch-swiping) that you can set ```data-bs-interval="false"``` to prevent the carousel from autoplaying.

+ **manage_crate**:
    + I implemented use of a session variable ```manage_crate``` which only sets to True when a user add or edits their crate contents on the supplies page and displays a summary of their crate in the notification.
        + This was working as intended but when being a user who had not initated the variable it was throwing a variety of errors trying to load ```supplies.html```.
        + My original troubleshooting was at the start of the ```all_supplies``` view; setting a variable ```manage_crate``` the None. This did not solve the problem.
    + I began searching around for how to check for the existence of a session variable and found [this post](https://stackoverflow.com/questions/10492819/checking-if-session-variable-is-set-or-not-in-django/10492856) which utilized the get method to make the code cleaner as no if/else statement was used.
        + The code displayed was:

            ```orderId = request.session.get('orderId',ts)```

            ```request.session['orderId']=ts```

        + I adapted this to check if ```manage_crate``` existed in the session variable and store the data in the view else set it to its current value (which is currently ```None```)

            ```manage_crate = request.session.get('manage_crate', manage_crate)```
            
            ```request.session['manage_crate'] = False```
        + The session variable is then set to ```False``` by default so that the crate summary only shows up in the intended notifications.
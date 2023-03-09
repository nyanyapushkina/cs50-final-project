# LEARNBYHEART
#
#### The project is shown only as an example. It's against CS50 policy: "The essence of all work that you submit to this course must be your own". You can learn more here: https://cs50.harvard.edu/x/2023/honesty/
#### Video Demo:  https://youtu.be/45-auyDy_P8
####
#### Description:
The idea of this web application is pretty simple: Learnbyheart is created for kids to make it easier to memorize poems. I remember myself being seven ish years old and crying over a poem i read over and over again in attempt to recite it at school tomorrow.
####
The project includes HTML, CSS and Python. I did give my choice a second thought, when I was implementing flipping cards. Turned out, JavaScript was probably the better way to do it. Anyway, I did it with card-flip and container classes:
```
<div class="card-flip">
    <div class="front d-flex flex-column align-items-center justify-content-center">
        <img src="/static/cardfacedown.png" alt="Card face down" class="img-fluid">
    </div>
    <div class="back d-flex flex-column align-items-center justify-content-center">
        <img class="card-img img-fluid" src="/static/cardfaceup.png" alt="Card face up with a piece of the poem">
            <div class="card-img-overlay">
                 <h4> {{ quatrain_1 }} </h4>
            </div>
    </div>
</div>
```

But first things first...

### Layout
HTML-file with the main structure. Is based on Bootstrap. My personal favourite touch is a little blue heart:
```
<a class="navbar-brand" href="/">
    LEARNBY
    <img src="/static/like.ico" alt="" width="26" height="26" class="d-inline-block align-baseline">
</a>
```
Navigation bar is pretty simple with two elements 'How to' and 'About' aligned left.

### Index
First page includes one text form for a user to type in a poem. There is only one button, too. Since the project was designed for kids, I wanted to keep it simple and clear. The mascot of the project is an elephant.
#
![Cartoon Elephant](https://img.freepik.com/free-vector/different-cute-illustrated-animals-collection_23-2148268753.jpg?w=1380&t=st=1676314899~exp=1676315499~hmac=9db17dbbb1f63fbd68fa206fda5084eef8f616ee85c40fa73d11771d7f19dd59)
#
I used a cartoon from Freepik. To overlap it over the input form, I used z-index for the image in CSS-file:
```
#elephant
{
    position: absolute;
    left: 960px;
    top: 410px;
    z-index: 2;
}
```
The overlap adds depth to the page, I think.

### app. py
The main part was to implement 'learn' function. It accepts the poem and, firstly, checks, if it meets the requirements and, secondly, divides a poem into quatrains to be displayed on cards. Other functions were created to display apologies and render pages.






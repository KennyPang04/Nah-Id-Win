# 312Team

Here is a link to our webapp!
https://nahidwin.org/

Authentication: Login/Logout<br>
Interactive Posts: Auction Page with like button (for now)<br>
Multimedia: Pictures for Auction Page<br>
Websockets: Global Chat<br>
Sense of Time: Global Chat can schedule chat messages<br>
DOS Protection: Done by Zhi<br>
Creativity: Done by ziyao, For creativity I implemented an dark mode feature where when you press the dark mode button your auth token for dark_mode gets set to true and then for all the different pages it will be serving you dark mode. This would be something extra that isn't required by any other objective for hw as none of them required you change the css based on what the user wanted.<br>
<br>
<br>
Testing Procedures:<br>
1. Navigate to the public deployment or localhost:8080 (if using docker) <br>
2a. Make sure the page loads in light mode <br>
2b. Check if the dark mode cookie is set to False <br>
3. Click the Dark Mode button under categories <br>
4a. Make sure the page reloads in dark mode <br>
4b. Check if dark mode cookie was set to True <br> 
5. Register & Login using dark mode <br>
6. After login navigate to the post button and click (bottom right) <br>
7. Check if the post page is loaded in dark mode <br>
8. Make a post and make sure the post is in dark mode <br>
9. Click the chat button and make sure global chat is also dark mode <br>
10. Make a chat to make sure everything works <br>
11. Exit the site <br>
12. Reload the website and make sure it is still in dark mode <br>

WARNING: some things might be broken due to unfamiliarity to hosting a webapp (everything works in testing I think)

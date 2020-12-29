import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {TweetFeedConponents,TweetConponents, TweetDetailComponent } from './tweets';
import {ProfileBadgeComponents} from './profiles'


const render_id = document.getElementById('root')

if (render_id) {
  ReactDOM.render(<App />, render_id);
}



const e = React.createElement

const our_id = document.getElementById('tweetme-2')
if (our_id) {
  ReactDOM.render(
    e(TweetConponents, our_id.dataset), our_id)
}


// selected using class
const tweetDetailElemenet = document.querySelectorAll(".tweetme-2-detail")
tweetDetailElemenet.forEach(container => {
  ReactDOM.render(
    e(TweetDetailComponent, container.dataset), container)

})

const our_feed_id = document.getElementById('tweetme-2-feed')
if (our_feed_id) {
  ReactDOM.render(
    e(TweetFeedConponents, our_feed_id.dataset), our_feed_id)
}


const our_profile_id = document.getElementById('tweetme-2-profile-badge')
if (our_profile_id) {
  ReactDOM.render(
    e(ProfileBadgeComponents, our_profile_id.dataset), our_profile_id)
}




// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

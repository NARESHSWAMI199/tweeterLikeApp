(this["webpackJsonptweetme2-web"]=this["webpackJsonptweetme2-web"]||[]).push([[0],{16:function(e,t,n){},17:function(e,t,n){"use strict";n.r(t);var c=n(0),a=n(1),s=n.n(a),r=n(4),i=n.n(r);n(16);function o(e,t,n,c){var a;c&&(a=JSON.stringify(c));var s=new XMLHttpRequest,r="http://localhost:8000/api".concat(t);s.responseType="json";var i=function(e){var t=null;if(document.cookie&&""!==document.cookie)for(var n=document.cookie.split(";"),c=0;c<n.length;c++){var a=n[c].trim();if(a.substring(0,e.length+1)===e+"="){t=decodeURIComponent(a.substring(e.length+1));break}}return t}("csrftoken");s.open(e,r),s.setRequestHeader("Content-Type","application/json"),i&&(s.setRequestHeader("X-Requested-With","XMLHttpRequest"),s.setRequestHeader("X-CSRFToken",i)),s.onload=function(){403===s.status&&"Authentication credentials were not provided."===s.response.detail&&(window.location.href="/login?show_login_requried=true"),n(s.response,s.status)},s.onerror=function(e){n({message:"the message was an error"},400)},s.send(a)}function l(e,t,n){var c="/tweet/";e&&(c="/tweet/?username=".concat(e)),null!==n&&void 0!==n&&(c=n.replace("http://localhost:8000/api","")),o("GET",c,t)}function u(e,t){var n="/tweet/feed/";null!==t&&void 0!==t&&(n=t.replace("http://localhost:8000/api","")),o("GET",n,e)}function d(e){var t=e.tweet,n=e.action,a=e.didPerformAction,s=t.likes?t.likes:0,r=n.display?n.display:"Action",i="likes"===n.display?"".concat(s," ").concat(n.display):r,l=e.className?e.className:"btn shadow-sm btn-primary",u=function(e,t){console.log("response ",e,"status ",t),200!==t&&201!==t||!a||a(e,t)};return Object(c.jsxs)("button",{className:l,onClick:function(e){e.preventDefault(),function(e,t,n){o("POST","/tweet/action/",n,{id:e,action:t})}(t.id,n.type,u)},children:["   ",i,"   "]})}var j=n(10),b=n(2);function f(e){var t=e.user,n=e.includeFullName,a=e.hidelink,r=!0===n?"".concat(t.first_name," ").concat(t.last_name):null;return Object(c.jsxs)(s.a.Fragment,{children:[r,!0===a?"@".concat(t.username):Object(c.jsxs)(m,{username:t.username,children:[" @",t.username," "]})]})}function m(e){var t=e.username;return Object(c.jsx)("span",{className:"pointer",onClick:function(e){window.location.href="api/profiles/".concat(t,"/follow/")},children:e.children})}function O(e){var t=e.user,n=e.hidelink,a=Object(c.jsx)("span",{className:"px-3 py-2 rounded-circle text-white bg-dark",children:t.username[0]});return!0===n?a:Object(c.jsx)(m,{username:t.username,children:a})}var w=n(9),h=n.n(w);function p(e){return Object(c.jsxs)("span",{className:e.className,children:[" ",h()(e.children).format("0a")," "]})}function x(e){var t=e.user,n=e.didFollowToggle,a=e.profileLoading,s=!0===(t&&t.is_following)?"Unfollow":"Follow";s=a?"loading...":s;return t?Object(c.jsxs)("div",{className:"container",children:[Object(c.jsx)("div",{className:"mb-3",children:Object(c.jsx)(O,{user:t,hidelink:!0,className:""})}),Object(c.jsxs)("div",{children:[Object(c.jsxs)("p",{children:["   ",Object(c.jsx)(f,{user:t,hidelink:!0,includeFullName:!0})," "]}),Object(c.jsxs)("p",{children:[Object(c.jsxs)(p,{children:[" ",t.follower_count]})," ",1===t.follower_count?"Follower":"Followers"," "]}),Object(c.jsxs)("p",{children:[Object(c.jsx)(p,{children:t.following_count})," Following "]}),Object(c.jsxs)("p",{children:[" ",t.location," "]}),Object(c.jsxs)("p",{children:[" ",t.bio," "]}),Object(c.jsxs)("button",{className:"btn btn-primary",onClick:function(e){e.preventDefault(),n&&!a&&n(s)},children:[" ",s," "]})]})]}):null}function v(e){var t=e.tweet;return t.parent?Object(c.jsx)(g,{retweeter:e.retweeter,isRetweet:!0,hideActions:!0,className:" ",tweet:t.parent}):null}function g(e){var t=e.tweet,n=e.didRetweet,r=e.hideActions,i=e.isRetweet,o=e.retweeter,l=Object(a.useState)(e.tweet?e.tweet:null),u=Object(b.a)(l,2),w=u[0],h=u[1],p=window.location.pathname,x=Object(j.a)(/([0-9]+)/,{tweetid:1}),g=p.match(x),N=g?g.groups.tweetid:-1,y="".concat(t.id)==="".concat(N),k=function(e,t){console.log("newAction tweet ",e,t),200===t?h(e):201===t&&n&&n(e)},T=e.className?e.className:"col-10 mx-auto p-3 col-md-6";return Object(c.jsxs)("div",{className:T,children:[!0===i&&Object(c.jsxs)("div",{className:"col-12 mb-3",children:[" ",Object(c.jsxs)("span",{className:"small text-muted",children:[" Retweet Via  @ ",Object(c.jsx)(f,{user:o})," "]}),"  "]}),Object(c.jsxs)("div",{className:"d-flex",children:[Object(c.jsx)(O,{user:t.user}),Object(c.jsxs)("div",{className:"col-11",children:[Object(c.jsx)(m,{username:t.user.username,children:Object(c.jsx)(f,{includeFullName:!0,user:t.user})}),Object(c.jsxs)("p",{children:[t.content," "]}),Object(c.jsx)(v,{tweet:t,retweeter:t.user})]})]}),Object(c.jsxs)("div",{className:"btn btn-group",children:[w&&!0!==r&&Object(c.jsxs)(s.a.Fragment,{children:[Object(c.jsx)(d,{tweet:w,didPerformAction:k,action:{type:"like",display:"likes"}}),Object(c.jsx)(d,{tweet:w,didPerformAction:k,action:{type:"unlike",display:"unlike"}}),Object(c.jsx)(d,{tweet:w,didPerformAction:k,action:{type:"retweet",display:"retweet"}})]}),!0===y?null:Object(c.jsx)("button",{className:" btn btn-sm btn-outline-primary",onClick:function(e){e.preventDefault(),window.location.href="/".concat(t.id)},children:" view "})]})]})}var N=n(3);function y(e){var t=Object(a.useState)([]),n=Object(b.a)(t,2),r=n[0],i=n[1],o=Object(a.useState)([]),u=Object(b.a)(o,2),d=u[0],j=u[1],f=Object(a.useState)(null),m=Object(b.a)(f,2),O=m[0],w=m[1],h=Object(a.useState)(!1),p=Object(b.a)(h,2),x=p[0],v=p[1];Object(a.useEffect)((function(){var t=Object(N.a)(e.newTweets).concat(r);t.length!==d.length&&j(t)}),[e.newTweets,d,r]),Object(a.useEffect)((function(){if(!1===x){l(e.username,(function(e,t){200===t?(w(e.next),i(e.results),v(!0)):alert("an error accur")}))}}),[r,x,v,e.username]);var y=function(e){var t=Object(N.a)(r);t.unshift(e),i(t);var n=Object(N.a)(d);n.unshift(d),j(n)};return Object(c.jsxs)(s.a.Fragment,{children:[d.map((function(e,t){return Object(c.jsx)(g,{tweet:e,didRetweet:y,className:"py-5 px-5 mt-1 border-radius shadow-sm  bg-white text-dark"},"".concat(t,"-{item.id}"))})),null!==O&&Object(c.jsx)("button",{onClick:function(t){if(t.preventDefault(),null!==O){l(e.username,(function(e,t){if(200===t){w(e.next);var n=Object(N.a)(d).concat(e.results);i(n),j(n)}else alert("an error accur")}),O)}},className:"btn mt-5 mb-5 btn-outline-primary",children:"Load More ..."})]})}var k=n(8);function T(e){var t=s.a.createRef(),n=e.didTweet,a=function(e,t){201===t?n(e):alert("data not sended to backend something went wrong")};return Object(c.jsxs)("div",{className:"container",children:[Object(c.jsx)("div",{className:"container mt-5 p-2",children:Object(c.jsx)("h1",{className:"offset-1",children:" Welcome on react tweets "})}),Object(c.jsx)("div",{className:e.className,children:Object(c.jsxs)("form",{onSubmit:function(e){e.preventDefault();var n=t.current.value;o("POST","/tweet/create/",a,{content:n}),t.current.value=""},children:[Object(c.jsx)("textarea",{ref:t,required:!0,className:"form-control",placeholder:" tweet here...."}),Object(c.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:" tweet "})]})})]})}function S(e){var t=Object(a.useState)([]),n=Object(b.a)(t,2),r=n[0],i=n[1],o=Object(a.useState)([]),l=Object(b.a)(o,2),d=l[0],j=l[1],f=Object(a.useState)(null),m=Object(b.a)(f,2),O=m[0],w=m[1],h=Object(a.useState)(!1),p=Object(b.a)(h,2),x=p[0],v=p[1];Object(a.useEffect)((function(){var t=Object(N.a)(e.newTweets).concat(r);t.length!==d.length&&j(t)}),[e.newTweets,d,r]),Object(a.useEffect)((function(){if(!1===x){u((function(e,t){200===t?(w(e.next),i(e.results),v(!0)):alert("an error accur")}))}}),[r,x,v,e.username]);var y=function(e){var t=Object(N.a)(r);t.unshift(e),i(t);var n=Object(N.a)(d);n.unshift(d),j(n)};return Object(c.jsxs)(s.a.Fragment,{children:[d.map((function(e,t){return Object(c.jsx)(g,{tweet:e,didRetweet:y,className:"py-5 px-5 mt-1 border-radius shadow-sm  bg-white text-dark"},"".concat(t,"-{item.id}"))})),null!==O&&Object(c.jsx)("button",{onClick:function(e){if(e.preventDefault(),null!==O){u((function(e,t){if(200===t){w(e.next);var n=Object(N.a)(d).concat(e.results);i(n),j(n)}else alert("an error accur")}),O)}},className:"btn mt-5 mb-5 btn-outline-primary",children:"Load More ..."})]})}function F(e){var t=Object(a.useState)([]),n=Object(b.a)(t,2),s=n[0],r=n[1],i="false"!==e.canTweet;return Object(c.jsxs)("div",{className:"container",children:[!0===i&&Object(c.jsx)(T,{didTweet:function(e){var t=Object(N.a)(s);t.unshift(e),r(t)},className:"col-10 offset-1"}),Object(c.jsx)(y,Object(k.a)({newTweets:s},e))]})}function E(e){var t=e.tweetId,n=Object(a.useState)(!1),s=Object(b.a)(n,2),r=s[0],i=s[1],l=Object(a.useState)(null),u=Object(b.a)(l,2),d=u[0],j=u[1],f=function(e,t){console.log("the status : ",e,t),200===t?j(e):alert("there is a error to finding your tweet")};return Object(a.useEffect)((function(){!1===r&&(!function(e,t){o("GET","/tweet/".concat(e,"/"),t)}(t,f),i(!0))}),[r,i,t]),null===d?null:Object(c.jsx)(g,{tweet:d,className:e.className})}var R=function(){return Object(c.jsxs)("div",{className:"container mt-5 p-5 ",children:[Object(c.jsx)("h1",{className:"offset-1",children:" Welcome on react tweets "}),Object(c.jsx)(F,{})]})},C=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,18)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,s=t.getLCP,r=t.getTTFB;n(e),c(e),a(e),s(e),r(e)}))},A=document.getElementById("root");A&&i.a.render(Object(c.jsx)(R,{}),A);var q=s.a.createElement,L=document.getElementById("tweetme-2");L&&i.a.render(q(F,L.dataset),L),document.querySelectorAll(".tweetme-2-detail").forEach((function(e){i.a.render(q(E,e.dataset),e)}));var P=document.getElementById("tweetme-2-feed");P&&i.a.render(q((function(e){var t=Object(a.useState)([]),n=Object(b.a)(t,2),s=n[0],r=n[1],i="false"!==e.canTweet;return Object(c.jsxs)("div",{className:"container",children:[!0===i&&Object(c.jsx)(T,{didTweet:function(e){var t=Object(N.a)(s);t.unshift(e),r(t)},className:"col-10 offset-1"}),Object(c.jsx)(S,Object(k.a)({newTweets:s},e))]})}),P.dataset),P);var _=document.getElementById("tweetme-2-profile-badge");_&&i.a.render(q((function(e){var t=e.username,n=Object(a.useState)(!1),s=Object(b.a)(n,2),r=s[0],i=s[1],l=Object(a.useState)(null),u=Object(b.a)(l,2),d=u[0],j=u[1],f=Object(a.useState)(!1),m=Object(b.a)(f,2),O=m[0],w=m[1],h=function(e,t){200===t&&j(e)};return Object(a.useEffect)((function(){!1===r&&(function(e,t){o("GET","/profiles/user/".concat(e,"/"),t)}(t,h),i(!0))}),[t,r,i]),!1===r?"loading...":d?Object(c.jsx)(x,{user:d,didFollowToggle:function(e){!function(e,t,n){var c={action:"".concat(t&&t).toLowerCase()};o("POST","/profiles/".concat(e,"/follow/"),n,c)}(t,e,(function(e,t){200===t&&j(e),w(!1)})),w(!0)},profileLoading:O}):null}),_.dataset),_),C()}},[[17,1,2]]]);
//# sourceMappingURL=main.6bb8a10b.chunk.js.map
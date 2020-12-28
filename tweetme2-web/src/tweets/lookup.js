import { backendLookup } from '../lookup'


export function apiTweetCreate(newTweet, callback) {
    backendLookup("POST", "/tweet/create/", callback, { content: newTweet })
}


export function apiTweetAction(tweetId,action, callback) {
    const data = { id : tweetId , action : action }
    backendLookup("POST", "/tweet/action/", callback, data)
}


export function apiTweetDetail(tweetId ,callback) {

    backendLookup("GET", `/tweet/${tweetId}/`, callback)
}




// xhr ajax request 
export function apiTweetList(username,callback,nextUrl) {
    let endpoint  = "/tweet/"
    if (username){
        endpoint = `/tweet/?username=${username}`
    }
    if (nextUrl !== null && nextUrl !== undefined){
        // replace method using for remove domain of site
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    backendLookup("GET",endpoint, callback)
}

export function apiTweetFeed(callback,nextUrl) {
    let endpoint  = "/tweet/feed/"   // HERE API IS ALLREADY INCULDE IN LOOKUP FOLDER' COMPONETS.JS
    if (nextUrl !== null && nextUrl !== undefined){
        // replace method using for remove domain of site
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    backendLookup("GET",endpoint, callback)
}


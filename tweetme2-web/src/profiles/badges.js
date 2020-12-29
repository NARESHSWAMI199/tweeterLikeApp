import { useState, useEffect } from 'react'
import { apiProfileDetail, apiProfileFollowToggle } from './lookup'
import { UserDisplay, UserPicture } from './components'
import { DisplayCount } from './utils'


export function ProfileBadge(props) {
    const { user, didFollowToggle, profileLoading } = props
    let currentVerb = (user && user.is_following) === true ? "Unfollow" : "Follow"
    currentVerb = profileLoading ? "loading..." : currentVerb

    const handleFollowToggle = (event) => {
        event.preventDefault()

        // we add here !profileLoading beacuse we need our data change only time   example  Follow or Unfollow
        if (didFollowToggle && !profileLoading) {
            didFollowToggle(currentVerb)
        }

    }
    return user ? <div className="container">
        <div className="mb-3">
            <UserPicture user={user} hidelink className="" />
        </div>
        <div>
            <p>   <UserDisplay user={user} hidelink includeFullName /> </p>
            <p><DisplayCount> {user.follower_count}</DisplayCount> {user.follower_count === 1 ? "Follower" : "Followers"} </p>
            <p><DisplayCount>{user.following_count}</DisplayCount> Following </p>
            <p> {user.location} </p>
            <p> {user.bio} </p>
            <button className="btn btn-primary" onClick={handleFollowToggle}> {currentVerb} </button>
        </div>
    </div> : null
}



export function ProfileBadgeComponents(props) {
    const { username } = props
    const [didLookup, setDidLookup] = useState(false)
    const [profile, setProfile] = useState(null)
    const [profileLoading, setProfileLoading] = useState(false)


    const handleBackendLookup = (response, status) => {
        if (status === 200) {
            setProfile(response)
        }
    }

    useEffect(() => {
        if (didLookup === false) {
            apiProfileDetail(username, handleBackendLookup)
            setDidLookup(true)
        }
    }, [username, didLookup, setDidLookup])

    const handleNewFollow = (actionVerb) => {
        apiProfileFollowToggle(username, actionVerb, (response, status) => {
            // here we will again set the setProfile beacuse this action perform on button click
            // console.log(response,status)
            if (status === 200) {
                setProfile(response)
            }
            setProfileLoading(false)
        })
        setProfileLoading(true)

    }
    return didLookup === false ? "loading..." : profile ? <ProfileBadge user={profile} didFollowToggle={handleNewFollow} profileLoading={profileLoading} /> : null
}
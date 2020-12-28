import React from 'react'

export function UserDisplay(props) {
    const { user, includeFullName } = props
    const fullname = includeFullName === true ? `` : null
    return <React.Fragment>
        {fullname}
        <span >@{user.username}</span>
    </React.Fragment>
}


export function UserLink(props) {
    const { username } = props
    // event is a defalut arg when you click a button or perfom and event
    const handleUserLink = (event) => {
        window.location.href = `profiles/${username}/`
    }
    return <span className="pointer" onClick={handleUserLink}>
        {props.children}
    </span>
}


// user pictrue calling in Tweet
export function UserPicture(props) {
    const { user } = props
    return <UserLink username={user.username} >
        <span className='px-3 py-2 rounded-circle text-white bg-dark' >{user.username[0]}</span>
    </UserLink>

}
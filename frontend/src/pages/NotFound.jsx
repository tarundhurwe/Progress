import React from 'react'
import NotFoundImage from "../assets/images/404_page_cover.jpg"

const NotFound = () => {
    return (
        <>
            <div className="card" style={{ width: "18 rem" }}>
                <img src={NotFoundImage} class="card-img-top" alt="Not Found" style={{ height: "99vh", width: "100%" }} />
            </div>
        </>
    )
}

export default NotFound
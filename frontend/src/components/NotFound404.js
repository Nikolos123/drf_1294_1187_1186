import React from 'react';

const NotFound404 = ({location}) =>{

    return(
        <div>
            <h2> Страница по адресу '{location.pathname}'</h2>
        </div>
    )
}

export  default  NotFound404;
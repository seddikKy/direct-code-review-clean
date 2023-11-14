import React from 'react';
import './Product.css'


function Product(props) {
    const { name, price, discount } = props;
    return (
        <div className="product">
            <div className="col">{name}</div>
            <div className="col">{price}</div>
            <div className="col">{discount}</div>
        </div>
    );
}

export default Product;

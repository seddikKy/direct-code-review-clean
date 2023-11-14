import React from 'react';

function PackageProduct(props) {
    const { name, price, discount, assets } = props;
    return (
        <div className="product">
            <div className="col">{name} - {assets} assets</div>
            <div className="col">{price}</div>
            <div className="col">{discount}</div>
        </div>
    );
}

export default PackageProduct;

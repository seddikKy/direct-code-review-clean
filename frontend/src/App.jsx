import {useEffect, useState} from "react";
import './App.css';
import Product from "./components/Product";
import PackageProduct from "./components/PackageProduct";
function App() {
const [productsDisplay, setProductsDisplay] = useState([]);
  useEffect(() => {
      fetch("http://0.0.0.0:5000/products/")
          .then(res => res.json())
          .then(
              (result) => {

                  let displays = []
                  for (let i = 0; i < result.products.length; i++) {
                      let product = result.products[i];

                      if (product.type == '1') {
                          displays.push(
                              <li key={i} style={{listStyle: 'none'}}>
                                  <Product {...product} />
                              </li>
                          )
                      } else if (product.type == '2') {

                          displays.push(
                              <li key={i} style={{listStyle: 'none'}}>
                                  <PackageProduct {...product} />
                              </li>
                          )
                      } else if (product.type == '3') {
                          let freeBanner = ''
                          if (product.price == 0) {
                              freeBanner = <span style={{ color: 'red' }}> Free</span>;
                          }
                          displays.push(
                              <li key={i} style={{listStyle: 'none'}}>
                                  <div className="product">
                                      <div className="col">{product.name}</div>
                                      <div className="col">{product.price} {freeBanner}</div>
                                      <div className="col">{product.discount}</div>
                                  </div>
                              </li>
                          )
                      }
                  }
                  setProductsDisplay(displays);
              },
              (error) => {
                  console.error(error)
              }
          )
  }, [])



    return (
       <div className="App">

           <h2>All Products</h2>
           <p><input/></p>
           <ul id="List" className="products">
               {productsDisplay.map((display, index) => (display))}
           </ul>

       </div>
    )
}

export default App;

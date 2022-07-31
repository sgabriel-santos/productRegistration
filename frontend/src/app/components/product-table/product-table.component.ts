import { Component, OnInit } from '@angular/core';
import { Product } from 'src/app/interfaces/product';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-product-table',
  templateUrl: './product-table.component.html',
  styleUrls: ['./product-table.component.scss']
})
export class ProductTableComponent implements OnInit {
  
  products: Product[] = [];

  constructor(private productService: ProductService) {}

  ngOnInit(): void {
    this.getProcucts();
  }

  getProcucts(): void {
    this.productService.getProducts()
        .subscribe(products => {
          this.products = products;
          console.log(products)
        });
  }

  delete(product_id: any): void {
    console.log(product_id)
    this.productService.deleteProduct(product_id).subscribe(_ => {
      this.products = this.products.filter(producct => producct.id !== product_id);
    })
  }
}

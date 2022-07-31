import { Component, OnInit } from '@angular/core';
import { ProductService } from 'src/app/services/product.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-product',
  templateUrl: './add-product.component.html',
  styleUrls: ['./add-product.component.scss']
})
export class AddProductComponent implements OnInit {
  product: any = {}
  category = ['Livro', 'Acessórios', 'Eletrônico']
  
  constructor(
    private productService: ProductService,
    private router: Router
    ) { }

  ngOnInit(): void {
  }

  onAddProduct(event: any){
    console.log(this.product)
    this.product.price = Number(this.product.price)
    this.productService.addProduct(this.product).subscribe(_ =>
      this.router.navigate(['/'])
    )
  }

}

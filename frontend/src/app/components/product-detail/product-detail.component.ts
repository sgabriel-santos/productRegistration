import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ProductService } from 'src/app/services/product.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.scss']
})
export class ProductDetailComponent implements OnInit {
  product: any = {};
  isUpdate: Boolean = true
  title = 'Alterar'
  category = ['Livro', 'Acessórios', 'Eletrônico', 'Fitness', 'Roupa']

  constructor(private route: ActivatedRoute,
    private productService: ProductService,
    private router: Router
  ) {}

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if(id){
      this.productService.getProduct(id)
      .subscribe(product =>  this.product = product);
    }else{
      this.title = 'Adicionar'
      this.isUpdate = false
    }
  }

  onChangeProduct(){
    if(this.isUpdate){
      this.updateProduct()
    }else{
      this.addProduct() 
    }
  }

  addProduct(){
    this.product.price = Number(this.product.price)
    this.productService.addProduct(this.product).subscribe(_ =>
      this.router.navigate(['/'])
    )
  }

  updateProduct(){
    this.productService.updateProduct(this.product, this.product.id).subscribe(_ =>
      this.router.navigate(['/'])
    )
  }
}

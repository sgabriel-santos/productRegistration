import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddProductComponent } from './components/add-product/add-product.component';
import { ProductDetailComponent } from './components/product-detail/product-detail.component';
import { ProductTableComponent } from './components/product-table/product-table.component';

const routes: Routes = [
  { path: '', component: ProductTableComponent},
  { path: 'detail/:id', component: ProductDetailComponent },
  { path: 'addProduct', component: AddProductComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

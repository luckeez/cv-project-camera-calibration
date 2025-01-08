## Idee Progetto

### 2D

Noi abbiamo fatto calibration della camera con punti 3d e relativi punti 2d.

Approccio tradizionale: prendere parametri intrinseci ed estrinseci della camera -> ricavare camera matrix.

https://chatgpt.com/share/677e4a9e-3ff0-8012-9a8a-f8ccb469aed7

- Definire **Intrinsic Matrix K**

![image-20250107194623083](/home/luckeez/.config/Typora/typora-user-images/image-20250107194623083.png)

fx, fy = focal lengths in pixels, s = skew (often 0), cx, cy = principal point (pixel coord, can be approximated as half the image width and height if no offsets are specified)

- dato che focal length probabilmente viene data in world units (mm), dobbiamo convertire in pixel units. (usare filmback properties, guardare chat) 

  ![image-20250108105303814](/home/luckeez/.config/Typora/typora-user-images/image-20250108105303814.png)

- nella chat c'è anche codice python per estrarre i valori (non funzionerà sicuro :) )

- Definire **Extrinsic Matrix** 

  ![image-20250107194750696](/home/luckeez/.config/Typora/typora-user-images/image-20250107194750696.png)

dove R = matrice di rotazione, t = vettore di traslazione (camera position in the world)

- **Projection Matrix finale**

![image-20250107194934564](/home/luckeez/.config/Typora/typora-user-images/image-20250107194934564.png)





### 3D

- aggiungere una seconda camera parallela e allineata alla prima

- calcolare disparità del punto desiderato (coordinata x a sinistra - coordinata x a destra)
- calcolare profondità Z

![image-20250103115522291](/home/luckeez/.config/Typora/typora-user-images/image-20250103115522291.png)

f = lunghezza focale, b = distanza tra le camere. **FISSI**

- calcolare coordinate X e Y

  ![image-20250103120800695](/home/luckeez/.config/Typora/typora-user-images/image-20250103120800695.png)

quindi

![image-20250107194359102](/home/luckeez/.config/Typora/typora-user-images/image-20250107194359102.png)

e

![image-20250107194420893](/home/luckeez/.config/Typora/typora-user-images/image-20250107194420893.png)



awdw

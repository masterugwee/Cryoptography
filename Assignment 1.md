## PART A  
### 2. 

#### Z5 =>

A | A-1
------------ | -------------
1 2 3 4 | 1 3 2


#### Z11 =>

A | A-1
------------ | -------------
 1 2 3 4 5 6 7 8 9 10 | 1 6 4 3 9 2 8 7 5 10



### 3. 
56245 = 43159 * 1 + 13086

43159 = 13086 * 3 + 3901

13086 = 3901 * 3 + 1383

3901 = 1383 * 2 + 1135

1383 = 1135 * 1 + 248

1135 = 248 * 4 + 143

248 = 143 * 1 + 105

143 = 105 * 1 + 38

105 = 38 * 2 + 29

38 = 29 * 1 + 9

29 = 9 * 3 + 2

9 = 2 * 4 + 1

2 = 1 * 2 + 0

###### GCD (56245, 43159) = 1

### 4. Compute phi(n) for 34 and 210

Phi (34 ) =>= 34 * (1 - 1/3)= 81 * 2/3=162 / 3= 54


Phi (210) =>
=210 * (1 - 1/2)
= 1024 * 1/2
= 512

### 5. Compute 3100 mod (31319)
Given, e=100

Therefore, 26+25+22

3^0 mod 31319 = 3

3^2 mod 31319 = 9

3^4 mod 31319 = 81

3^8 mod 31319 = 6561

3^16 mod 31319 = 14418

3^32 mod 31319 = 21979

3^64 mod 31319 = 12185

3^100 mod (31319) =

###### 12185 * 21979 * 81 mod 31319 = 5346 * 81 mod 31319 = 25879

## Part B - Programming Assignment
### 1.

```python
def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i
print("Modular multiplicative Inverse is ",mod_Inv( int(input()),int(input())))
```

(a) 53947-1 mod 56211

###### Modular multiplicative Inverse is  7225

(b) 9385-1 mod 431592

###### Modular multiplicative Inverse is  376729

### 2.
```python
from des import DesKey
for i in range(18446744073709551616): 
         s = str(hex(i)) 
         key = DesKey(bytes(s.zfill(16),encoding='utf8')) 
         ciptext = "4B518774A408E3E5" 
         hex_deco = bytes.fromhex(ciptext) 
         plaintext = key.decrypt(hex_deco,padding = True) 
         text = plaintext.decode('utf8',errors = 'ignore').strip() 
         if(len(text) >= 3): 
             print(text) 
```

### 3.

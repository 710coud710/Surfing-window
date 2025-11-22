file check:
Có giá trị "MP" trong test program, "MP" ở sau dấu _ thứ 2

```bash
Test Program        :Hapuka_ADL1_MP_V1.1.csv
```

# algorithm

            get trim_mfg data: }--> tm trim_mfg
              >>> 
              >>> 
              >>> <info> [00001447]   <---current trim value
              >>> mfg_data: 0x0A050000   <---comparative value
we need to compare "0x0A050000" is "0xFFFFFFFF" or not
if yes, need to sort out those DSN, including HokI and Hapuka ADL1 all the ADL1 MP test log

**character capture example:**
```bash
INFO Mon 09:09:32.914 [test_secure_provision.py:673 ] get trim_mfg data: }--> tm trim_mfg
	>>> 
	>>> 
	>>> <info> [00001447] current trim value: 
	>>> mfg_data: 0xFFFFFFFF   
    
```
**example not catch:**
```bash
   INFO Mon 09:09:32.914 [test_secure_provision.py:673 ] get trim_mfg data: }--> tm trim_mfg
	>>> 
	>>> 
	>>> <info> [00001447] current trim value: 
	>>> mfg_data: 0x0A050000
```
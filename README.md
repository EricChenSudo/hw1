(1) how to setup and run your program<br>

    1. Read the csv file and load the information into a variable called data.
    
    2. first, preprocessing the data.
    
        In TEMP column, change '-99.000' or '-999.00' with 'None'.
        The target_data will be used to store the answer, so we need to get the space first.
        And because the answer need to be arranged in the lexicographical order, I declare them first.
        After arranged the order, I made up the remaining space needed in the back of each elements.
        (I assume the maximum temperature of each stations are 'None' first.)
        
    3. Start to find the result in each station.
    
        The methods I used are
        
        1. Use for loop to let me can scan through all the station.
        
        2. check whether  the temperature of station[i] is 'None' or not.
            If the temperature of the station[i] is 'None', we can skip directly to check the next station,
            because we assume the temperature of the station is 'None' already.
            
        3. If the temperature of the station[i] isn't 'None', we need to check which one is bigger, 
           the temperature stored in the target_data or the temperature of the station[i].
        
        4. Finally, store the bigger one into the target_data.(Remember, station_ID should be the same)
            (NOTE)Because the datatype of the temperature stored in the data list is string, 
                  we need to convert it to float.
            (NOTE)If the temperature stored in the target_data is 'None' and the temperature of the station[i] 
                  isn't'None', we can assign the temperature of the station[i] to the target data directly.
            
(2) What are the result<br>

    The result is [['C0A880', 21.2], ['C0F9A0', 21.3], ['C0G640', 21.1], ['C0R190', 30.3], ['C0X260', 27.7]], when input file is 107061237.csv.
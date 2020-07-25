reference_game_build_details = build_info.clone()
    cheap_game_build_details = build_info.clone()
    
    reference_game = ClickerState()
    cheap_game = ClickerState()
    
#    reference_game.set_history(history)
#    cheap_game.set_history(history)
#    
    #first update yhe history to the reference game
    for item in history:
        
#        print item
        
        if item[1] != None:
        
            item_cost = item[2]
        
            wait_time = item[0] - reference_game.get_time()
            
#            print
#            print item_cost
#            print wait_time
            
            reference_game.wait(wait_time)
            cheap_game.wait(wait_time)
            
            reference_game.buy_item(item[1], item_cost, reference_game_build_details.get_cps(item[1]))
            cheap_game.buy_item(item[1], item_cost, cheap_game_build_details.get_cps(item[1]))

#            reference_game_build_details.update_item(item[1])
#            cheap_game_build_details.update_item(item[1])
    
#    print
#    print reference_game
#    print cheap_game
#    
    expensive_item = strategy_expensive(cookies, cps, history, time_left, reference_game_build_details)
#    print expensive_item
    
    cheap_item = strategy_cheap(cookies, cps, history, time_left, cheap_game_build_details)
#    print cheap_item
    
    if expensive_item != None:
        
        item_cost = reference_game_build_details.get_cost(expensive_item)
        
        wait_time = reference_game.time_until(item_cost)
        
        reference_game.wait(wait_time)
        
        reference_game.buy_item(expensive_item, item_cost, reference_game_build_details.get_cps(expensive_item))
#        
        reference_game_build_details.update_item(expensive_item)
        
        while cheap_game.get_time() <= reference_game.get_time():
            
            cost = cheap_game_build_details.get_cost(cheap_item)
            
            time = cheap_game.time_until(cost)
            
            if cheap_game.get_time() + time > reference_game.get_time():
                break
            
            cheap_game.wait(time)
            
            cheap_game.buy_item(cheap_item, cost, cheap_game_build_details.get_cps(cheap_item))
            
            cheap_game_build_details.update_item(cheap_item)
        
#        print cheap_game.get_time(), reference_game.get_time()
        
        if cheap_game.get_time() < reference_game.get_time():
            cheap_game.wait(reference_game.get_time() - cheap_game.get_time())
        
#        reference_game.wait(0.01 * wait_time)
#        cheap_game.wait(0.01 * wait_time)
        
#    print reference_game
#    print cheap_game
    
    cps_growth_rate = cheap_game.get_cps() / reference_game.get_cps()
    total_cookies_growth_rate = cheap_game.get_total_cookies() / reference_game.get_total_cookies()
    
#    print cps_growth_rate, total_cookies_growth_rate
    
    if cps_growth_rate < 1 and round(total_cookies_growth_rate * 100000) <= 100000:
        best_item = expensive_item
    else:
        best_item = cheap_item
    
#    print best_item
    
    return best_item
#    return "Cursor"
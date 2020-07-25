"""
the following code is a part of my first strategy function
it had a problem of forgetting history of purchases
"""

reference_game = ClickerState()
    
    build_details = build_info.clone()
#    print reference_game
    
    expensive_item = strategy_expensive(cookies, cps, history, time_left, build_details)
    cheap_item = strategy_cheap(cookies, cps, history, time_left, build_details)
    
#    cost = build_info.get_cost(cheap_item)
#    print cost
#    
#    time = clicker_state.time_until(cost)
#    
#    clicker_state.wait(time)
#    
#    print clicker_state
#    
#    clicker_state.buy_item(item, build_info.get_cost(item), build_info.get_cps(item))
#    
#    build_info.update_item(item)
    if expensive_item != None:
        cost = build_details.get_cost(expensive_item)
    
        time = reference_game.time_until(cost)
    
        reference_game.wait(time)
    
        reference_game.buy_item(expensive_item, build_info.get_cost(expensive_item), build_info.get_cps(expensive_item))
#    
        build_details.update_item(expensive_item)
    
        cheap_game = simulate_clicker(build_details, time, strategy_cheap)
    
        reference_game_cps = reference_game.get_cps()
        reference_game_total_cookies = reference_game.get_total_cookies()
    
        cheap_game_cps = cheap_game.get_cps()
        cheap_game_total_cookies = cheap_game.get_total_cookies()
    
    #comparing growth rates of both games
        cps_growth_rate = cheap_game_cps / reference_game_cps
        total_cookies_growth_rate = cheap_game_total_cookies / reference_game_total_cookies
    
    #test cases for each line
#    print build_details.build_items()
#    print
#    print reference_game.get_cps()
#        print expensive_item, cost, time
#        print
        print reference_game
        print reference_game_cps, reference_game_total_cookies
        print
        print cheap_game
        print cheap_game_cps, cheap_game_total_cookies
        print 
        print cps_growth_rate, total_cookies_growth_rate
        print cps_growth_rate < 1, total_cookies_growth_rate < 1
    
    #deciding the best growth rate item
        if cps_growth_rate < 1  and total_cookies_growth_rate < 1:
            best_item = expensive_item
        else:
            best_item = cheap_item
#    
        print best_item
        print
        return best_item
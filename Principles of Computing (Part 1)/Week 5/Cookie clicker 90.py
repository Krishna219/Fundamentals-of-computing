"""
Cookie Clicker Simulator
"""

#import simpleplot
import math

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        initializes ClickerState class
        """
        self._total_number_of_cookies = 0.0
        self._current_number_of_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history_list = [ (0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        msg = ""
        msg += "Time : " + str(self._current_time) + " "
        msg += "Current cookies : " + str(self._current_number_of_cookies) + " "
        msg += "CPS : " + str(self._current_cps) + " "
        msg += "Total cookies : " + str(self._total_number_of_cookies) + " "
        msg += "History : " + str(self._history_list)
        return msg
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_number_of_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history_list)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_number_of_cookies < cookies:
            time_to_given_cookies = (cookies - self._current_number_of_cookies) / self._current_cps
            whole_time = math.ceil(time_to_given_cookies)
            return float(whole_time)
        else:
            return 0.0
        
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time += time
            self._current_number_of_cookies += self._current_cps * time
            self._total_number_of_cookies += self._current_cps * time
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_number_of_cookies >= cost:
            self._current_number_of_cookies -= cost
            self._current_cps += additional_cps
            self._history_list.append((self._current_time,
                                       item_name,
                                       cost,
                                       self._total_number_of_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    build_details = build_info.clone()
    
    clicker_state = ClickerState()
    
    while clicker_state.get_time() <= duration:
        item = strategy(clicker_state.get_cookies(),
                        clicker_state.get_cps(),
                        clicker_state.get_history(),
                        duration - clicker_state.get_time(),
                        build_details)
        
        if item == None:
            break
        
        cookies = build_details.get_cost(item)
        
        time = clicker_state.time_until(cookies)
        
        if clicker_state.get_time() + time > duration:
            break
            
        clicker_state.wait(time)
        
        clicker_state.buy_item(item, cookies, build_details.get_cps(item))
        
        build_details.update_item(item)
    
    if clicker_state.get_time() < duration:
        clicker_state.wait(duration - clicker_state.get_time())
    
    return clicker_state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    cost = float('inf')
#    cost = 6
    cheapest_item = None
    
#    print build_info.build_items()
    
#    for item in build_info.build_items():
#        print build_info.get_cost(item)
    for item in build_info.build_items():
        
        if build_info.get_cost(item) < cost:
#            print build_info.get_cost(item)
#            print cost
#            print build_info.get_cost(item) < cost
            cost = build_info.get_cost(item)
            cheapest_item = item
    
    max_cookies = time_left * cps + cookies
    
#    print cheapest_item, max_cookies, cost
    
    if cost <= max_cookies:
        return cheapest_item
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    affordable_items = {}
    
    max_cookies = time_left * cps + cookies
#    print max_cookies
    
    for item in build_info.build_items():
        if build_info.get_cost(item) <= max_cookies:
            #storing all possible affordable items in a dictionary that maps
            #cost to item
            affordable_items[build_info.get_cost(item)] = item
    
#    print affordable_items
    
    if len(affordable_items.keys()) > 0:
#        print affordable_items[max(affordable_items.keys())]
        return affordable_items[max(affordable_items.keys())]
    else:
        return None
        

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15), time, strategy)
    print strategy_name, ":", state
    print

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

#    history = state.get_history()
#    history = [((item[0]), (item[3])) for item in history]
#    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
#    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    


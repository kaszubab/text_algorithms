#!/usr/bin/env python
# coding: utf-8

# In[206]:


def naive_substring_search(text, pattern):
    
    occurences_array = []
    
    for s in range(0, len(text) - len(pattern) + 1):
        if text[s:s+len(pattern)] == pattern:
            occurences_array.append(s)
    return occurences_array
    



# In[208]:




def prepare_automata(pattern):
    alphabet_symbols = set(pattern)
    transition_table = []
    
    lps = 0
    
    for i in range(len(pattern)+1):
        transition_table.append({})
        if i == 0:
            for x in alphabet_symbols:
                transition_table[i][x] = 0
            transition_table[i][pattern[i]] = 1
        else:    
            for x in alphabet_symbols:
                transition_table[i][x] = transition_table[lps][x]
            if i < len(pattern):
                transition_table[i][pattern[i]] = i+1
                lps = transition_table[lps][pattern[i]]
    return transition_table
    
    


# In[210]:


def finite_automata_matching(text, pattern):
    trans_array = prepare_automata(pattern)
    shift_arr = []
    state = 0
    for i in range(len(text)):
        try:
            state = trans_array[state][text[i]]
        except:
            state = 0
        if state == len(pattern):
            shift_arr.append( i+1-state)
    return shift_arr


# In[213]:


def compute_prefix_array(pattern):
    prefix_array = [-1,0]
    i = 2
    j = 0
    while i <= len(pattern):
        if pattern[i-1] == pattern[j]:
            prefix_array.append(j+1)
            i += 1
            j += 1
        elif j > 0:
            j = prefix_array[j]
        else:
            prefix_array.append(0)
            i += 1
    return prefix_array
    
    


# In[214]:


def kmp_matching(text, pattern):
    prefix_array = compute_prefix_array(pattern)
    shift_array = []
    text_pos = 0
    pat_pos = 0
    
    while text_pos + pat_pos < len(text):
        
        if pattern[pat_pos] == text[text_pos+pat_pos]:
            pat_pos += 1
            if pat_pos == len(pattern):
                shift_array.append(text_pos)                
                text_pos += pat_pos - prefix_array[pat_pos]
                pat_pos = prefix_array[pat_pos-1]
        else:
            text_pos = text_pos + pat_pos - prefix_array[pat_pos]
            if pat_pos > 0:
                pat_pos = prefix_array[pat_pos]            
    
    return shift_array
        

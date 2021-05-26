def zip_lists(ll1, ll2):
  current1 = ll1.head
  current2 = ll2.head
  ll1_lead = current1.next
  ll2_lead = current2.next
  current1.next = current2

  running = True
  while running:
    current2.next = ll1_lead
    if ll1_lead.next is None:
      ll1_lead.next = ll2_lead
      running = False
      break
    if ll2_lead.next is None:
      ll2_lead.next = ll1_lead.next
      ll1_lead.next = ll2_lead
      running = False
      break
    ll1_lead = ll1_lead.next
    current1 = current2.next
    current1.next = ll2_lead
    current2 = current1.next
    ll2_lead = ll2_lead.next
  
  ll2.head = None
  return 'babies'


# 7. while running:
# 8. set current2.next = ll1_lead
# 9. check to see if ll1_lead.next is equal to None
# 10.             if ll1_lead.next is equal to None then set ll1_lead.next equal to      ll2_lead
# 11.             and then set running equal to False and break
# 12. check to see if ll2_lead.next is equal to None
# 13.             if it is, then set ll2_lead.next equal to ll1_lead.next,
# 14.             then set ll1_lead.next equal to ll2_lead,
# 15.             then set running = False and then break
# 16. set ll1_lead = ll1_lead.next
# 17. set current1 = current2.next
# 18. set current1.next = ll2_lead
# 19. set current2  = current1.next
# 20. set ll2_lead = ll2_lead.next
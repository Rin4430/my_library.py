def test_load():
  return 'loaded'
def naive_bayes(table, evidence_row, target):
  #compute P(target=0|...) by using cond_prob_product, take the product of the list, finally multiply by P(target=0) using cond_prob
  neg_1 = cond_probs_product(table, evidence_row, target, 0) * prior_prob(table, target, 0)

  #do same for P(target=1|...)
  pos_1 = cond_probs_product(table, evidence_row, target, 1) * prior_prob(table, target, 1)

  #Use compute_probs to get 2 probabilities
  neg,pos = compute_probs(neg_1, pos_1)
  #return your 2 results in a list
  return [neg, pos]
  def cond_probs_product(table,evidence_row,target,target_value):
  table_columns = up_list_column_names(table) #your function body below
  evidence_columns = table_columns[:-1]
  evidence_complete = up_zip_lists(evidence_columns, evidence_row)
  cond_prob_list = [cond_prob(table, evidence_column, evidence_value, target, target_value) for evidence_column, evidence_value in evidence_complete]
  partial_numerator = up_product(cond_prob_list)
  return partial_numerator
  def cond_prob(table,evidence,evidence_value,target,target_value):
  t_subset = up_table_subset(table, target, 'equals', target_value)
  e_list = up_get_column(t_subset, evidence)
  p_b_a = sum([1 if v==evidence_value else 0 for v in e_list])/len(e_list)
  return p_b_a
  def prior_prob(table, target, target_value):
  t_list = up_get_column(table, target)
  p_a = sum([1 if v==target_value else 0 for v in t_list])/len(t_list)
  return p_a
  def compute_probs(neg,pos):
  p0 = neg/(neg+pos)
  p1 = pos/(neg+pos)
  return [p0,p1]

class global_var():
    # 定义case 的列 id . openpyxl第一列就是1。所以数组第一列为Null,从index(1)开始
    var_arr = []  # 1   2       3   4       5
    var_arr = ["NULL", "ID", "model", "is_check", "id_comment", "id_key", "id_by",
               "id_value", "id_dependent_key", "dependent_method", "checkresult"]


def get_id_col():
    return global_var.var_arr.index("ID")


def get_model_col():
    return global_var.var_arr.index("model")


def get_id_comment_col():
    return global_var.var_arr.index("id_comment")


def get_id_key_col():
    return global_var.var_arr.index("id_key")


def get_id_by_col():
    return global_var.var_arr.index("id_by")


def get_id_value_col():
    return global_var.var_arr.index("id_value")


def get_id_dependent_key_col():
    return global_var.var_arr.index("id_dependent_key")


def get_dependent_method():
    return global_var.var_arr.index("dependent_method")


def get_checkresult_col():
    return global_var.var_arr.index("checkresult")

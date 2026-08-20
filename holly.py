
for i in range(1, 10):
    # 內層迴圈：j 代表乘數，從 1 到 9
    for j in range(1, 10):
        # 使用 f-string 格式化輸出，\t 表示 Tab 鍵對齊
        print(f"{i}x{j}={i*j:2d}", end="\t")
    # 當內層迴圈跑完 1~9 後，換行進入下一個 i
    print()
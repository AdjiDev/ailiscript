# gradient_colors.py

def rgb_gradient(start_color, end_color, steps):
    """
    Membuat gradient warna dari start_color ke end_color dalam steps tertentu.
    
    :param start_color: tuple RGB warna awal (R, G, B)
    :param end_color: tuple RGB warna akhir (R, G, B)
    :param steps: jumlah langkah atau tingkat gradien
    :return: List warna gradien dalam bentuk ANSI escape code
    """
    gradient = []
    
    r_step = (end_color[0] - start_color[0]) / steps
    g_step = (end_color[1] - start_color[1]) / steps
    b_step = (end_color[2] - start_color[2]) / steps
    
    for i in range(steps + 1):
        r = int(start_color[0] + (r_step * i))
        g = int(start_color[1] + (g_step * i))
        b = int(start_color[2] + (b_step * i))
        
        ansi_code = f"\033[38;2;{r};{g};{b}m"
        gradient.append(ansi_code)
    
    return gradient

def apply_gradient_to_text(text, gradient):
    """
    Menerapkan gradient warna ANSI pada teks.
    
    :param text: Teks yang akan diberi warna gradien
    :param gradient: List kode warna ANSI
    :return: Teks yang diberi warna gradien
    """
    colored_text = ""
    gradient_steps = len(gradient)
    text_len = len(text)
    
    step_size = gradient_steps / text_len
    
    for i, char in enumerate(text):
        gradient_index = int(i * step_size)
        colored_text += gradient[gradient_index] + char
    
    return colored_text + "\033[0m"  


if __name__ == "__main__":
    start_color = (255, 0, 0)   
    end_color = (255, 0, 255)   
    text = "Gradient from Red to Magenta"
    
    gradient = rgb_gradient(start_color, end_color, len(text))
    colored_text = apply_gradient_to_text(text, gradient)
    
    print(colored_text)

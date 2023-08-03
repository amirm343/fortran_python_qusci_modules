
function tp(a, b) result(c)
    implicit none
    
    real(kind=8), intent(in)    :: a(:, :)
    real(kind=8), intent(in)    :: b(:, :)
    real(kind=8)    :: c(size(a, 1)*size(b, 1),size(a, 2)*size(b, 2))
    integer k, l, i, j

    do k= 1, size(a, 1), 1
        do l= 1, size(b, 1), 1
            do i= 1, size(a, 2), 1
                do j= 1, size(b, 2), 1
                    c((k-1)*(size(b, 1))+l, i*(size(b, 2)-1)+j)= a(k, i)*b(l, j)
                end do
            end do
        end do
    end do
 
end function tp